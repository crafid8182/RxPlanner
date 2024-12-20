import { useState } from "react";
import "./Start.css";

const Start = () => {
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
                    <input type="text" placeholder = "First Name"/>
                </div>

                <div className = "input">
                    <input type="text" placeholder = "Age"/>
                </div>

                <div className = "input">
                    <input type="text" placeholder = "Weight"/>
                </div>

                <div className = "input">
                    <input type="text" placeholder = "Ethnicity"/>
                </div>

            </div>
            <div className = "submit-container">
                <div className = "submit">
                    <button>Submit</button>
                </div>
            </div>
          </div>
        </>
    )
}

export default Start