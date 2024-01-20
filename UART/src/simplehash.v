module simplehash(
    output reg [7:0] hash_output,   
    input wire [7:0] data_input 
);

    always @* begin
        hash_output = data_input ^ 8'h55;         
    end
endmodule

