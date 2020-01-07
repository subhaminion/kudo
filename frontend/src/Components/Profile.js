import React from "react";
import Navbar from './Navbar';
import Mykudos from './Mykudos';
import Userlist from './Userlist';


const Profile = props => (
	<div>
		<Navbar />
	    <Mykudos />
	    <Userlist />
	</div>  
);
export default Profile;