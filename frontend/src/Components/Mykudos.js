import React from "react";
import { getToken } from '../utils'

class Mykudos extends React.Component {
	constructor() {
		super();
		this.state = {
			kudoList: []
		}
	}
	componentDidMount() {
      fetch('http://localhost:8000/api/kudo/', {
         method: 'get',
         headers: {
           'Content-Type':'application/json',
           'Authorization': getToken(),
         }
      }).then(response => response.json())
      .then(json => {
          this.setState({
            kudoList: json
          })
      });
    }
	render() {
		return (
			<div className="col-xs-6">
			<h2 className="sub-header">Recieved Kudo</h2>
			  <div className="table-responsive">
	            <table className="table table-striped">
	              <thead>
	                <tr>
	                  <th className="col-md-2">Header</th>
	                  <th className="col-md-2">Message</th>
	                </tr>
	              </thead>
	              <tbody>
	                {this.state.kudoList.map((item, i) => (
                            <tr key={i}>
                              <td className="col-md-1">{item.kudos_header}</td>
                              <td className="col-md-1">{item.kudos_message}</td>
                            </tr>
                      ))}
	              </tbody>
	            </table>
	          </div>
			</div>
		)
	} 
};
export default Mykudos;