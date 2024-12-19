import { useState } from "react";


function Start() {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleUsernameChange = (e) => {
        e.preventDefault();
        
        const response = fetch('http://localhost:3001/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username, password}),
        });

    };

    return (
        <>
            
            <h1>Get started by filling out some basic information!</h1>

            <form>
                <div>
                    <label>Username:</label>
                    <input type="text" id='username'>
                    </input>
                </div>
                <div>
                    <label>Password:</label>
                    <input type="password" id='password'>
                    </input> 
                </div>
            </form>


        </>
    );
}

export default Start