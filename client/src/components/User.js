import React, { Component } from "react";
import "../styles/user.css";

class User extends Component {
    changeUser = () => {
        const user =this.props.user
        this.props.changeUser(user);
        console.log("user",  this.props.changeUser);
    };

    render() {
        const user = this.props.user;
        return (
            <div className="profile-container" onClick={this.changeUser}>
                <p>{user.name}</p>
                    <img
                        className="profile-avatar"
                        src={user.avatar}
                        alt={user.name}
                    />
            </div>
        );
    }
}

export default User;
