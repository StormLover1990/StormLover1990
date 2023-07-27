import React from "react";

const DogDetails = ({ dog }) => {
  return (
    <div>
      <h1>{dog.name}</h1>
      <img src={dog.src} alt="A dog" />
      <p>Age: {dog.age}</p>

      <ul>
        <h3>Facts:</h3>
        {dog.facts.map((fact) => (
          <li key={fact}>{fact}</li>
        ))}
      </ul>
    </div>
  );
};

export default DogDetails;
