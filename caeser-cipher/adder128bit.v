module fulladder_behav(sum,carry,a,b,c);
output reg[127:0] sum,carry;
input[127:0] a,b,c;
always@(a or b or c)
begin
if(a==0&&b==0)
begin sum =0;carry = 0;
end
else if(a==0&&b == 1)
begin sum =1;carry = 0;
end
else if(a==1&&b == 0)
begin sum =1;carry = 0;
end
else if(a==1&&b == 1)
begin sum =1;carry =1;
end
end
endmodule
