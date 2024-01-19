module main
(
    output TxD,
    
    input RxD,
    input clock,
    input reset,
    input transmit 
);

wire [7:0] recieve;

// intermediate variable
// reg [7:0] RxData;
 
Reciever(recieve, clock, reset, RxD);
Transmitter(TxD, clock, recieve, transmit , reset );

endmodule