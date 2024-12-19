import { useState } from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

//components
import Head from "./components/Head.jsx";
import Main from "./components/Main.jsx";
import Start from "./components/Start.jsx";




function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <Head />


      <Router>
        <Routes>

        <Route path="/" element={<Main />} />
        <Route path="/start" element={<Start />} />

        </Routes>
      </Router>
    </>
  );
}

export default App;