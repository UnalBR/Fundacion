-- MySQL Workbench Synchronization
-- Generated: 2022-09-01 11:09
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: bstev

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER TABLE `fundacionsherman`.`Agendamiento` 
DROP FOREIGN KEY `fk_Agendamiento_Transaccion1`;

ALTER TABLE `fundacionsherman`.`Entidad_salud` 
DROP FOREIGN KEY `fk_Entidad_salud_Usuarios1`;

ALTER TABLE `fundacionsherman`.`Agendamiento` 
DROP FOREIGN KEY `fk_Agendamiento_Usuarios1`;

ALTER TABLE `fundacionsherman`.`Agendamiento` ADD CONSTRAINT `fk_Agendamiento_Usuarios1`
  FOREIGN KEY (`Usuarios_ID usuario`)
  REFERENCES `fundacionsherman`.`Usuarios` (`ID usuario`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_Agendamiento_Transaccion1`
  FOREIGN KEY (`Transaccion_idTransaccion`)
  REFERENCES `fundacionsherman`.`Transaccion` (`idTransaccion`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `fundacionsherman`.`Entidad_salud` 
ADD CONSTRAINT `fk_Entidad_salud_Usuarios1`
  FOREIGN KEY (`Usuarios_ID usuario`)
  REFERENCES `fundacionsherman`.`Usuarios` (`ID usuario`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
