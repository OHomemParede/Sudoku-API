import { Router } from "express";
import SudokuController from "@controllers/SudokuController";

const router: Router = Router();

router
    .route("/sudoku/:difficulty")
    .post(SudokuController.generateSudoku);

export { router }; 