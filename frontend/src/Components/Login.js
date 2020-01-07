import React from "react";
import {
	Redirect
} from "react-router-dom";
import { isLogin } from '../utils';


class Login extends React.Component {
    constructor() {
        super();
        this.state = {
            username: "",
            password: "",
            responsemsg: ""
        }
    }

    login = () => {
    	let data = JSON.stringify({
		    "username": this.state.username,
		    "password": this.state.password
		   })
    	fetch('http://localhost:8000/api/login/', {
		   method: 'post',
		   headers: {
		   	'Content-Type':'application/json'
		   },
		   body: data 
		}).then(response => response.json())
          .then(json => {
            this.setState({
                responsemsg: json.msg
            })
          	if (json.token != null) {
                localStorage.setItem('token', json.token)
                window.location = "/profile";
            }
        });
    }

    handleUsernameChange = (ev) => {
    	this.setState({
    		username: ev.target.value
    	})
    }

    handlePasswordChange = (ev) => {
    	this.setState({
    		password: ev.target.value
    	})
    }

    render() {
    	if (isLogin()) {
    		return <Redirect to="/profile" />;
    	}
        return (
        <div>
		  	<h2>Login</h2>

			  <div className="imgcontainer">
			    <img src="https://www.w3schools.com/howto/img_avatar2.png" alt="Avatar" className="avatar" />
			  </div>

			  <div className="container">
                  <h3>{this.state.responsemsg}</h3>
			    <label htmlFor="uname"><b>Username</b></label>
			    <input value={this.state.username} onChange={this.handleUsernameChange.bind(this)} type="text" placeholder="Enter Username" name="uname" required />

			    <label htmlFor="psw"><b>Password</b></label>
			    <input value={this.state.password} onChange={this.handlePasswordChange.bind(this)} type="password" placeholder="Enter Password" name="psw" required />
			        
			    <button type="submit" onClick={this.login}>Login</button>
			  </div>
	  </div>
        )
    }
}

export default Login;