module Receiver(
output [7:0] RxData,
   
input clock_fpga,
input reset,
input RxD
    );

// Internal variables
reg shift;
reg state, nextstate;
reg [3:0] bit_counter;
reg [1:0] sample_counter;
reg [13:0] baudrate_counter;
reg [9:0] rxshift_reg;
reg clear_bitcounter, inc_bitcounter, inc_samplecounter, clear_samplecounter; 


// baudrate_counter
parameter clk_freq = 100_000_000; 
parameter baud_rate = 9_600;
parameter div_sample = 4;
parameter div_counter = clk_freq/(baud_rate * div_sample);
parameter mid_sample = (div_sample/2);
parameter div_bit = 10; 


assign RxData = rxshift_reg [8:1]; 
// UART

// UART
always@(posedge clock_fpga)
    begin

        if (reset)begin
        
            state <= 0;
            bit_counter <= 0;
            baudrate_counter <= 0;
            sample_counter <= 0;
        end else begin
            baudrate_counter <= baudrate_counter + 1;
            if (baudrate_counter >= div_counter - 1) begin
                baudrate_counter <= 0;
                state <= nextstate ; 
                
                if (shift)rxshift_reg <= {RxD,rxshift_reg[9:1]};
                if (clear_samplecounter) sample_counter <= 0;
                if (inc_samplecounter) sample_counter <= sample_counter + 1;
                if (clear_bitcounter) bit_counter <= 0;
                if (inc_bitcounter) bit_counter <= bit_counter + 1;
            end
        end
    end

always@(posedge clock_fpga )
begin
    
    shift <= 0;
    clear_samplecounter <=0;
    inc_samplecounter <=0;
    clear_bitcounter <=0;
    inc_bitcounter <=0;
    nextstate <=0;
         
    case (state)
        0:  begin
    
           if(RxD )
            begin
            nextstate <= 0;
            end
           else begin
                nextstate <= 1;
                clear_bitcounter <= 1;
                clear_samplecounter<= 1;
           end
        end
    
        1:  begin
            nextstate <= 1;
            if (sample_counter == mid_sample-1) shift <= 1;
               if (sample_counter  == div_sample-1) begin 
                   if (bit_counter == div_bit -1) begin
                nextstate <= 0;
                end
            
                inc_bitcounter <= 1;
                clear_samplecounter <= 1;
            end
            
            else
            begin
                inc_samplecounter <= 1;
            end
        end 
    default: nextstate <= 0;
    endcase

end

endmodule