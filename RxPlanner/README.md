  function handleAPI() {

    const formData = new FormData();
    formData.append('image', img)
    axios.post('http://localhost:5001/api/img', formData).then((res) => {
      console.log(res);
    })
  }