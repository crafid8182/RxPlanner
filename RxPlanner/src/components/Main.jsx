import { useNavigate } from "react-router-dom";
import Start from "./Start.jsx";

function Main() {

    const navigate = useNavigate();

    const handleNavigate = () => {
        navigate("/Start");
    };

  return (
    <>
      <h1>Health starts with RxPlanner!</h1>
      <div className="card">
        <button onClick = {handleNavigate}>
            Start Your Journey
        </button>
      </div>
    </>
  );
}

export default Main;