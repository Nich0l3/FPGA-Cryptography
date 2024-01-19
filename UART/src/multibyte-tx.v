`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 01/17/2024 09:42:05 AM
// Design Name: 
// Module Name: multibyte-tx
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module multibytetx(
    input clock,
    input [15:0] data,
    input transmit,
    input reset,
    output reg TxD
    );
    
    // internal varibales 
    reg [3:0] bit_counter; // start + data + stop = 10 bits, 16 bits to store them 
    reg [13:0] baudrate_counter; // 2^14 =16K, clks/bit = 100MHz/9600Hz = 10K (internal/required)
    reg [9:0] shiftright_register; // storing 10 bit data 
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
                shiftright_register <= {1'b1, tempdata[7:0] ,1'b0}; // 10 bits are loaded 
                tempdata <= tempdata >> 8;
            end
                
            if (clear) // clear is asserted
                bit_counter<=0; // basically do nothing :)
            
            if (shift) // shift signal is asserted 
            begin    
                shiftright_register <= shiftright_register >> 1; // pushing the data out of register, LSB first !!!
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
        
        if (bit_counter == 10) // All data has been transmitted 
        begin
            next_state = 0; // TX -> IDLE mode
            clear <= 1; // clear bit counter
        end
        
        else // Data is left in register 
        begin
            next_state <= 1; // Tx -> TX mode
            TxD <= shiftright_register [0]; // TxD line sends the data
            shift <= 1; // continuing shifting the data so that new bit arrives at the LSB 
        end     
   
        end
      
    default : next_state <= 0; // IDLE -> IDLE
    
    endcase
    
    
    
    end
     


endmodule
