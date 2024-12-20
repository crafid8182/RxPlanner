import reactLogo from '/Users/moeraff/Documents/Coding/rx-project/RxPlanner/src/assets/react.svg'
import '/Users/moeraff/Documents/Coding/rx-project/RxPlanner/src/App.css'


//RxLogo Component used as the header
function Head() {

  return (
    <>
      <div>

        <a href="/" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>

    </>
  )
}

export default Head