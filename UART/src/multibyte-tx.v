module multibytetx(

    output reg TxD,
    
    input transmit,
    input clock,
    input reset,
    input [15:0] data
 
    );
    
    // internal varibales 
    reg [4:0] bit_counter; // start + data + stop = 10 bits * 2 = 20, 20 bits to store them 
    
    reg [13:0] baudrate_counter; // 2^14 =16K, clks/bit = 100MHz/9600 = 10K (internal/required)
    
    reg [9:0] shiftright_register_1; // storing 1st byte 
    reg [9:0] shiftright_register_2; // storing 2nd byte 
    
    reg state, next_state; // swtich between idle mode and transmission mode 
    
    reg shift; // shift signal to start shifting
    reg load; // load signal to start loading data  
    reg clear; // reset bit_counter for UART transmission 
    
    reg [15:0]tempdata; 
    
 // UART transmission 
    always@(posedge clock)
    begin
    
    if(reset)
    begin
        tempdata <= data; 
        state<=0; // IDLE state 
        bit_counter<=0; // counter for bit tx is set to 0 
        baudrate_counter<=0;
    end
    
    else
    begin
    baudrate_counter <= baudrate_counter + 1;
    
        if (baudrate_counter == 10415)
        begin
            state<=next_state; // IDLE -> Tx state 
            baudrate_counter<=0; // reset itself
            
            if (load) // load is asserted
            begin
                shiftright_register_1 <= {1'b1, tempdata[7:0] ,1'b0}; // 10 bits are loaded
                shiftright_register_2 <= {1'b1, tempdata[15:8] ,1'b0}; // 10 bits are loaded
                 
                // tempdata <= tempdata >> 8;
            end
                
            if (clear) // clear is asserted
                bit_counter<=0; // basically do nothing :)
            
            if (shift) // shift signal is asserted 
            begin   
                if (bit_counter < 10)
                    shiftright_register_1<= shiftright_register_1 >> 1; // pushing the data out of register, 1st byte!!!
                else
                    shiftright_register_2 <= shiftright_register_2  >> 1; // pushing the data out of register, 2nd byte!!!
                    
                bit_counter <= bit_counter + 1;
            end
        end
    end
           
    end

// Mealy Machine , State machine 

    always@(posedge clock)
    begin
    
    // initialize 
    load <= 0;
    shift <= 0;
    clear <= 0;
    TxD <= 1; // when set to 1, there is no transmission in progress
    
    case(state) 
    0:  begin //IDLE
        
        if (transmit) // transmit is asserted
        begin
            next_state <= 1; // IDLE -> Tx mode
            load <= 1;
            shift <= 0;
            clear <= 0;
        end
        
        else
        begin
            next_state <= 0; // IDLE -> IDLE mode
            TxD <= 1; // no TX, remains high for no TX 
        end
        
        
        end
    
    1:  begin // TX
        
        if (bit_counter == 20) // All data has been transmitted 
        begin
            next_state = 0; // TX -> IDLE mode
            clear <= 1; // clear bit counter
        end
        
        else // Data is left in register 
        begin
            next_state <= 1; // Tx -> TX mode
            
            if (bit_counter < 10)
                TxD <= shiftright_register_1 [0]; // TxD line sends the data
            else   
                TxD <= shiftright_register_2 [0];
            shift <= 1; // continuing shifting the data so that new bit arrives at the LSB 
        end     
   
        end
      
    default : next_state <= 0; // IDLE -> IDLE
    
    endcase
    
    
    
    end
     


endmodule