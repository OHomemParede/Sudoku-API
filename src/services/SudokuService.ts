import { spawn } from "child_process";
import { Response } from "express";
import path from "path";

const sudokuPath = path.join(__dirname, "../../src/services/sudoku");

class SudokuService {
    generateSudoku(difficulty: string, res: Response): void {
        const sudokuProcess = spawn("python", [sudokuPath, difficulty]);

        sudokuProcess.stdout.on("data", (data: Buffer) => {
            let sudokuText: string = data.toString();
            sudokuText = sudokuText.replace(/'/g, '"');

            const sudokuJson: JSON = JSON.parse(sudokuText);

            res.status(200).json(sudokuJson);
        });
    }
}

export default new SudokuService();