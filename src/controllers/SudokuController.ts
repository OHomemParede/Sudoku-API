import { Request, Response } from "express";
import SudokuService from "@services/SudokuService";

class SudokuController {
    generateSudoku(req: Request, res: Response) {
        const { difficulty } = req.params;
        try {
            if (
                !Number.isInteger(Number(difficulty)) ||
                Number(difficulty) < 0 ||
                Number(difficulty) > 81
            )
                return res
                    .status(400)
                    .json({
                        "Parameter Error": "[difficulty] must be an integer | 0<=[difficulty]<= 81",
                    });

            SudokuService.generateSudoku(difficulty, res);

        } catch (error: any) {
            console.error(error);
            return res.status(500).json({ error: error.message });
        }
    }
}

export default new SudokuController();
