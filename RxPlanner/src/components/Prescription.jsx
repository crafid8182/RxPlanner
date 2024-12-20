import { useLocation } from "react-router-dom";
import { useState } from "react";
import "./Prescription.css";
import axios from "axios";

const Prescription = () => {
  const location = useLocation();
  const details = location.state || {};

  const [img, setImg] = useState('');

  function handleImage(event) {
      console.log(event.target.files);
      setImg(event.target.files[0]);
  }

  function handleAPI() {

    const formData = new FormData();
    formData.append('image', img)
    axios.post('http://localhost:5001/api/img', formData).then((res) => {
      console.log(res);
    })
  }

  return (
    <>
      <div className="container">
        <div className="text">{details.advisory}</div>

        <h4>Upload an image of your prescription and we'll build a tracker so you never have to worry again</h4>

        <input onChange= {handleImage}
        className="upload" type="file" name="myFile" accept=".png,.jpg,.jpeg" />

        <div  onClick = {handleAPI} className="submit-container">
          <div className="submit">
            Upload Prescription Image
          </div>
        </div>

      </div>
    </>
  );
};

export default Prescription;
