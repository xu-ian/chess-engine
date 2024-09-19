CREATE SCHEMA `chess_engine`;
CREATE TABLE `chess_engine`.`stored_moves` (
  `side` VARCHAR(5) NOT NULL,
  `board_state` VARCHAR(200) NOT NULL,
  `depth` INT NOT NULL,
  `move` VARCHAR(20) NOT NULL,
  `value` VARCHAR(200) NOT NULL,
  CONSTRAINT `pkey` PRIMARY KEY (`side`,`board_state`, `depth`)
);

insert into chess_engine.stored_moves (side,board_state, depth,move) values("black","abcdef",4,"unknown");