module main
(
    output TxD,
    
    input RxD,
    input clock,
    input reset,
    input transmit 
);

wire [7:0] recieve;
wire [7:0] dummy;

wire [7:0] shift; 
assign shift = 8'b1; 

// intermediate variable
// reg [7:0] RxData;
 
Reciever(recieve, clock, reset, RxD);

ceasar_cipher(dummy,recieve,shift);

Transmitter( TxD, clock, dummy, transmit , reset );

endmodule