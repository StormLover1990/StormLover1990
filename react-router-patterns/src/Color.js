import React from "react";
import { useParams } from "react-router-dom";
import colorList from "./colorList";

const Color = () => {
  const { name } = useParams();
  const color = colorList.find((colorObj) => colorObj.name === name);
  // console.log(color);
  return (
    <>
      <h1>{color.name}</h1>
      <div
        className="colorCircle"
        style={{
          backgroundColor: `${color.color}`,
          borderColor: "black",
          height: "5em",
          width: "5em",
          marginLeft: "50%",
        }}
      ></div>
    </>
  );
};

export default Color;
