import { useNavigate } from "react-router-dom";
import "./Main.css";

//Component that serves as the Introduction to RxPlanner
function Main() {

    const navigate = useNavigate();

    //Function that navigates to start your Journey
    const handleNavigate = () => {
        navigate("/Start");
    };

  return (
    <>
      <h1>Health starts with RxPlanner!</h1>
      <div className="card">

        {/* Starts your Journey when you click by using handleNavigation */}
        <button className="start"onClick = {handleNavigate}>
            Start Your Journey
        </button>
      </div>
    </>
  );
}

export default Main;