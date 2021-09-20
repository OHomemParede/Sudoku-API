import express, { Request, Response } from 'express';
import { router } from "./routes"
import dotenv from "dotenv";
dotenv.config();


class Server {
    public app: express.Application;
    public port: number;

    constructor() {
        this.app = express();
        this.port = parseInt(process.env.PORT || "3000");
        this.init();
    }

    init() {
        try {
            this.app.use("/api", router);
            this.app.use((req: Request, res: Response) => {
                res.status(400).json({ error: "Unknown URL" });
            });

            this.app.listen(this.port, () => {
                console.info(`Listening at http://localhost:${this.port}`);
            });

        } catch (error) {
            console.error({ error });
        }
    }
}

export default new Server();