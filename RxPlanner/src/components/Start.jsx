import { useState } from "react";
import "./Start.css";

const Start = () => {

    const [details, setDetails] = useState({
        name: "",
        age: "",
        height: "",
        weight: "",
        ethnicity: ""
    });

    const handleChange = (event) => {
        const {name, value} = event.target;
        setDetails((prev) => {
            return {...prev, [name]: value}
        })
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log(details);

        fetch('http://localhost:5001/api/submit', {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(details)
        })

    }

    return (
        <>
          <h1>Get started by filling out some basic information!</h1>
    
          <div className="container">
            <div className = "header">
                <div className = "text">Sign Up</div>
                <div className = "underline"></div>
            </div>

            
            <div className = "inputs">

                <div className = "input">
                    <input type="text" placeholder = "First Name" name="name" onChange= {handleChange}/>
                </div>

                <div className = "input">
                    <input type="text" placeholder = "Age" name="age" onChange= {handleChange}/>
                </div>

                <div className = "input">
                    <input type="text" placeholder = "Height" name="height" onChange= {handleChange}/>
                </div>

                <div className = "input">
                    <input type="text" placeholder = "Weight" name="weight" onChange= {handleChange}/>
                </div>

                <div className = "input">
                    <input type="text" placeholder = "Ethnicity" name="ethnicity" onChange= {handleChange}/>
                </div>

            </div>
            <div className = "submit-container">
                <div className = "submit" onClick = {handleSubmit}>
                    Submit
                </div>
            </div>
          </div>
        </>
    )
}

export default Start