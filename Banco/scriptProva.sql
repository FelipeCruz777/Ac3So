drop database so;
create database so;
use so;

create table pessoa(
	idPessoa int auto_increment primary key,
	nomePessoa varchar(30),
	idade int 
);

select * from pessoa;
insert into pessoa values (null,"Cruz",18);