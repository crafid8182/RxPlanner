import { useLocation } from "react-router-dom";
import { useState } from "react";
import "./Prescription.css";
import axios from "axios";

const Prescription = () => {
  
  // inherits data from previous page's API request to the backend
  const location = useLocation();
  const details = location.state || {};

  const [img, setImg] = useState('');

  //only one file at a time so index = 0
  function handleImage(event) {
      console.log(event.target.files);
      setImg(event.target.files[0]);
  }

  //backend gets processed img and return ical file that can be downloaded
  function handleAPI() {
    const formData = new FormData();
    formData.append('image', img);
  
    axios.post('http://localhost:5001/api/img', formData, {
      responseType: 'blob' // Important to handle binary file response
    })
    .then((res) => {
      // Create a blob URL and trigger the download
      const url = window.URL.createObjectURL(new Blob([res.data]));
      const link = document.createElement('a');
      link.href = url;
  
      // Set the file name for the download
      const contentDisposition = res.headers['content-disposition'];
      const filename = contentDisposition
        ? contentDisposition.split('filename=')[1]
        : 'prescription-reminder.ics';
  
      link.setAttribute('download', filename.replace(/['"]/g, '')); // Remove any quotes
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    })
    .catch((err) => {
      console.error(err);
    });
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
