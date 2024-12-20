import { useLocation } from "react-router-dom";
import "./Prescription.css";

const Prescription = () => {
  const location = useLocation();
  const details = location.state || {};

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(details);
  };

  return (
    <>
      <div className="container">
        <div className="text">{details.advisory}</div>

        <h4>Upload an image of your prescription and we'll build a tracker so you never have to worry again</h4>

        <input className="upload" type="file" name="myFile" accept=".png,.jpg,.jpeg" />

        <div className="submit-container">
          <div className="submit">
            Upload Prescription Image
          </div>
        </div>

      </div>
    </>
  );
};

export default Prescription;
