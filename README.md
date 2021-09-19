# Sudoku api

![Typescript](https://img.shields.io/badge/-Typescript-1572B6?style=flat-square&logo=typescript&logoColor=white "Typescript")
![Python](https://img.shields.io/badge/-Python-2b5b84?style=flat-square&logo=Python&logoColor=white "Python")
![Nodejs](https://img.shields.io/badge/-Nodejs-339933?style=flat-square&logo=Node.js&logoColor=white "Node.js")
![Express](https://img.shields.io/badge/-Express-339933?style=flat-square&logo=Express&logoColor=white "Express")

## Setup Service
```bash
 yarn && yarn build
 ```

## Run Service
```bash
yarn start
```

## About Sudoku Service
- _path_: src/services/sudoku 
  
- _language_: Python

- _description_: Takes a single input x, and returns a random matrix from the set of possible sudoku matrices. This algorithm is mapped to a set of possibilities, such algorithms are called "Non-Deterministic Algorithms", besides this algorithm does not have all the possibilities already pre-calculated, but generates one of the possible configurations, which saves memory, but it costs additional computational time.

- _input (CLI)_: must receive a single value x that belongs to the set valid_x = { x ∈ Z+: 0≤x≤81 }.

- _output (stdout)_: Return a string in JSON format, detailed below.

 | Key              | Type   | Description                      |
 | ---------------- | ------ | -------------------------------- |
 | `generator_time` | number | Time in seconds it took to generate a matrix. |
 | `rows_length`    | number | Number of rows in the matrix. |
 | `columns_length` | number | Numbers of columns in the matrix. |
 | `original_matrix`| array  | Generated `rows_length` by `columns_length` matrix. |
 | `game_matrix`    | array  | It's a copy of `original matrix`, but has random picks of coordinate points assigned to zero, you should use this matrix for gameplay.|
