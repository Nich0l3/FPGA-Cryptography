module main
(
    output TxD,
    
    input RxD,
    input clock,
    input reset,
    input transmit 
);

wire [7:0] receive;
wire [7:0] dummy;

wire [7:0] shift; 
assign shift = 8'b1; 

// intermediate variable
// reg [7:0] RxData;
 
Receiver(receive, clock, reset, RxD);

//ceasar_cipher(dummy,receive,shift);
simplehash(dummy, receive);

Transmitter( TxD, clock, dummy, transmit , reset );

endmodule