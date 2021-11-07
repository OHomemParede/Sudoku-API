import { Router } from "express";
import SudokuController from "@controllers/SudokuController";

const router: Router = Router();

router
    .route("/sudoku/:difficulty")
    .get(SudokuController.generateSudoku);

export { router }; 
