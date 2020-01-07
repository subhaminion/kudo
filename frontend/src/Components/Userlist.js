import React from "react";
import { getToken } from '../utils'
import Modal from "./Modal";

class Userlist extends React.Component {
    constructor() {
        super();
        this.state = {
          userList: [],
          show: false,
          kudos_header: '',
          kudos_message: '',
          toSendUserId: '',
          responsemsg: ""
        }
    }

    showModal = e => {
      this.setState({
        show: !this.state.show,
        responsemsg: "Enter Kudo Details"
      });
    };

    setUserId = e => {
      this.setState({
        toSendUserId: e.target.getAttribute('user-id')
      })
    }

    componentDidMount() {
      fetch('http://localhost:8000/api/user/', {
         method: 'get',
         headers: {
           'Content-Type':'application/json',
           'Authorization': getToken(),
         }
      }).then(response => response.json())
      .then(json => {
          console.log(json)
          this.setState({
            userList: json
          })
      });
    }

    sendKudos = () => {
      let data = JSON.stringify({
        "kudos_header": this.state.kudos_header,
        "kudos_message": this.state.kudos_message,
        "to_user": this.state.toSendUserId
       })
      fetch('http://localhost:8000/api/kudo/', {
         method: 'post',
         headers: {
           'Content-Type':'application/json',
           'Authorization': getToken(),
         },
         body: data 
      }).then(response => response.json()
        .then(json => {
          this.setState({
            responsemsg: json.msg,
            kudos_header: '',
            kudos_message: ''
          })
        }));
    }

    handleKudoheaderChange = (ev) => {
        this.setState({
          kudos_header: ev.target.value
        })
    }

    handleKudomessageChange = (ev) => {
      this.setState({
        kudos_message: ev.target.value
      })
    }

    render() {
       return (
            <div className="col-xs-6">
                  <h2 className="sub-header">All Users</h2>
                  <div className="table-responsive">
                    <table className="table table-striped">
                      <thead>
                        <tr>
                          <th className="col-md-1">username</th>
                          <th className="col-md-1">organization</th>
                          <th className="col-md-1">Action</th>
                        </tr>
                      </thead>
                      <tbody>
                     {this.state.userList.map((item, i) => (
                            <tr key={i}>
                              <td className="col-md-1">{item.username}</td>
                              <td className="col-md-1">{item.orgranization.name}</td>
                              <td className="col-md-1">
                                <button className="btn-sm btn-primary toggle-button"
                                  id="centered-toggle-button"
                                  user-id={item.id}
                                  onClick={e => {
                                    this.showModal(e)
                                    this.setUserId(e)
                                  }}
                                >
                                  Give Kudo
                                </button>
                              </td>
                            </tr>
                      ))}
                        
                      </tbody>
                    </table></div>
                    <Modal onClose={this.showModal} show={this.state.show} responsemsg={this.state.responsemsg}>
                      <div>
                      <div className="form-group">
                        <input type="text" value={this.state.kudos_header} onChange={this.handleKudoheaderChange.bind(this)} className="form-control" placeholder="Enter Header" id="kudoheader" />
                      </div>
                      <div className="form-group">
                        <input type="text" value={this.state.kudos_message} onChange={this.handleKudomessageChange.bind(this)} className="form-control" placeholder="Enter message" id="message" />
                      </div>
                      <button className="btn btn-success" onClick={this.sendKudos}> Send </button>
                      </div>
                    </Modal>
            </div>
       )
    }
}

export default Userlist;