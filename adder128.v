`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 20.01.2024 16:59:13
// Design Name: 
// Module Name: adder128
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


module adder128 (output part0,part1,part2,part3,part4,part5,part6,part7,part8,part9,part10,part11,part12,part13,part14,part15,
input [127:0]input_sig
    );
    
reg [7:0] part0, part1, part2, part3,part4,part5,part6,part7,part8,part9,part10,part11,part12,part13,part14,part15;
always @(input_sig)
   {part15, part14, part13, part12, part11, part10, part9, part8, part7, part6, part5, part4, part3, part2, part1, part0} = input_sig;
endmodule
