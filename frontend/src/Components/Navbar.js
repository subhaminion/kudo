import React from "react";
import { getToken, logout } from '../utils'

class Navbar extends React.Component {
	constructor() {
		super();
		this.state = {
			username: '',
			orgranization: ''
		}
	}
	componentDidMount() {
      fetch('http://localhost:8000/api/me/', {
         method: 'get',
         headers: {
           'Content-Type':'application/json',
           'Authorization': getToken(),
         }
      }).then(response => response.json())
      .then(json => {
          this.setState({
            username: json[0].username,
            orgranization: json[0].orgranization.name
          })
      });
    }
    signOut = () => {
    	logout();
        window.location = "/";
    }
	render() {
		return (
			  <nav className="navbar navbar-inverse">
		      <div className="container-fluid">
		        <div className="navbar-header">
		          <a className="navbar-brand" href="#">UserName: {this.state.username}</a>
		          <a className="navbar-brand" href="#">Organization: {this.state.orgranization}</a>
		          <a className="navbar-brand" href="#" onClick={this.signOut}>Log Out</a>
		        </div>
		      </div>
		    </nav> 
		)
	} 
};
export default Navbar;