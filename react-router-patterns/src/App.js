import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import DogList from "./DogList";
import NotFound from "./NotFound";
import Colors from "./Colors";
import Color from "./Color";
import Home from "./Home";
import ColorForm from "./ColorForm";
function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="dogs/*" element={<DogList />} />
          <Route path="*" element={<NotFound />} />
          <Route path="colors/" element={<Colors />} />
          <Route path="colors/:name" element={<Color />} />
          <Route path="colors/new" element={<ColorForm />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
