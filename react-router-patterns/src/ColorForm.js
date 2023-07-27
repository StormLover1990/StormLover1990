import React, { useState } from "react";
import { v4 as uuid } from "uuid";
import { Navigate } from "react-router-dom";

const ColorForm = ({ addColor }) => {
  const [formData, setFormData] = useState({
    name: "black",
    color: "#000000",
  });
  const handleChange = (evt) => {
    const { name, value } = evt.target;
    setFormData((formData) => ({
      ...formData,
      [name]: value,
    }));
  };
  const gatherInput = (evt) => {
    evt.preventDefault();
    addColor(...formData);
    setFormData({ name: "black", color: "#000000" });
  };
  return (
    <div>
      {formData && <Navigate to="/colors" replace={true} />}
      <form onSubmit={gatherInput}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            onChange={handleChange}
            type="text"
            name="name"
            value={formData.name}
            id={uuid()}
          />
        </div>
        <div>
          <label htmlFor="color">Color:</label>
          <input
            onChange={handleChange}
            type="color"
            name="color"
            value={formData.color}
            id={uuid()}
          />
        </div>
        <button>Add Color</button>
      </form>
    </div>
  );
};
export default ColorForm;
