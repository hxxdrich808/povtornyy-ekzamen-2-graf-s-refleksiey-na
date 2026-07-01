# Graph with Reflection on Code

This project demonstrates a simple graph data structure and its visualization using D3.js.  
The graph supports adding nodes, directed edges, and reflexive edges (self‑loops).  
The UI renders the graph in an SVG canvas with a force‑directed layout.

## Features

- Pure JavaScript implementation (no Python or other languages).
- Reflexive edges can be added automatically.
- Interactive visualization with drag support.
- Simple test suite using Jest.

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://git.brojs.ru/kuzakhmetovartur/povtornyy-ekzamen-2-graf-s-refleksiey-na.git
   cd povtornyy-ekzamen-2-graf-s-refleksiey-na
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Run the application**

   ```bash
   npm start
   ```

   Open your browser at `http://localhost:3000` (or the port shown in the console).

4. **Run tests**

   ```bash
   npm test
   ```

## Project Structure

```
├── public
│   └── index.html          # Entry point for the browser
├── src
│   ├── index.js            # Application bootstrap
│   ├── graph.js            # Graph data structure
│   └── ui.js               # Rendering logic
├── __tests__
│   └── graph.test.js       # Jest tests for Graph
├── package.json
└── README.md
```

## License

MIT License