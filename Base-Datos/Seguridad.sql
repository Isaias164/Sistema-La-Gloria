#CREO LOS ROLES
CREATE ROLE PROGRAMADOR,DISEÑADOR,ADMINISTRADOR;

#CREO LOS PERMISOS QUE VAN A TENER LOS ROLES
GRANT CREATE,REFERENCES,INSERT,SELECT ON la_gloria.* TO "DISEÑADOR";
GRANT EXECUTE,EVENT,SELECT,INSERT,UPDATE,TRIGGER,CREATE ROUTINE ON la_gloria.* TO "PROGRAMADOR";
GRANT ALL PRIVILEGES ON la_gloria.* TO "ADMINISTRADOR"

#CREOS LOS USUARIOS
#ADMINISTRADOR
CREATE USER "JUAN"@"%" IDENTIFIED BY "MARIAKUKA123";
CREATE USER "CARLOS"@"%" IDENTIFIED BY "20204ÑOM4LD1TO";
#PROGRAMADOR
CREATE USER "ISAIAS"@"localhost" IDENTIFIED BY "L4570R7UG45N1NLL45";
CREATE USER "JESICA"@"localhost" IDENTIFIED BY "90K3M0NG0";
#DISEÑADOR
CREATE USER "BELINDA"@"192.168.0.6" IDENTIFIED BY "ABDUZCAN12345";
CREATE USER "MATIAS"@"192.168.0.6" IDENTIFIED BY"C4B4LL3R05D3LZ0D14C0";

#ASIGNO LOS PERMISOS A LOS USUARIOS
#ADMINISTRADORES
GRANT ADMINISTRADOR TO "JUAN"@"%";
GRANT ADMINISTRADOR TO "CARLOS"@"%";
#PROGRAMADORES
GRANT PROGRAMADOR TO "ISAIAS"@"localhost";
GRANT PROGRAMADOR TO "JESICA"@"localhost";
#DISEÑADOR
GRANT DISEÑADOR TO "BELINDA"@"localhost";
GRANT DISEÑADOR TO "BELINDA"@"localhost";
