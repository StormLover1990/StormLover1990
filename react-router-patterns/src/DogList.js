import React from "react";
import DogDetails from "./DogDetails";
import defaultProps from "./defaultProps";
import { Link } from "react-router-dom";
import NotFound from "./NotFound";
import Home from "./Home";
import { Routes, Route } from "react-router-dom";
const [whiskey, duke, perry, tubby] = defaultProps.dogs;

const DogList = () => {
  return (
    <>
      <nav>
        <Link to="/dogs">Home</Link>
        <Link to="whiskey">Whiskey</Link>
        <Link to="duke">Duke</Link>
        <Link to="perry">Perry</Link>
        <Link to="tubby">Tubby</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="whiskey" element={<DogDetails dog={whiskey} />} />
        <Route path="duke" element={<DogDetails dog={duke} />} />
        <Route path="perry" element={<DogDetails dog={perry} />} />
        <Route path="tubby" element={<DogDetails dog={tubby} />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  );
};
export default DogList;
