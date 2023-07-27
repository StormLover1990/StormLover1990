import React, { useState } from "react";
import { Link, Route, Routes } from "react-router-dom";
import colorList from "./colorList";
import ColorForm from "./ColorForm";

import { v4 as uuid } from "uuid";

const Colors = () => {
  const [colors, setColors] = useState(colorList);
  const addColor = (color) => {
    let newColor = { ...color, id: uuid() };

    setColors((colors) => [...colors, newColor]);
  };

  return (
    <div>
      <>
        <h1>Colors</h1>
        <ul>
          {colors.map((color) => (
            <li key={uuid()}>
              <Link to={`${color.name}`}>{color.name}</Link>
            </li>
          ))}
          <li key={uuid()}>
            <Link to="new">Add Color</Link>
          </li>
        </ul>
      </>
    </div>
  );
};
export default Colors;
