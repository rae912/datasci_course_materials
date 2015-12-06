-- (g) multiply 2874
select * from A where row_num = 2;
select * from B where col_num = 3;
select a.value * b.value from A a, B b where a.row_num = 2 and b.col_num=3 and a.col_num=b.row_num;
select sum(mul) from (select a.value * b.value as mul from A a, B b where a.row_num = 2 and b.col_num=3 and a.col_num=b.row_num);