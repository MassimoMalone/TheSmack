import React from "react";
import "./Profile.css";
import profileImage from "../assets/defaulticon.png";
import CreateSmack from "../pages/CreateSmack";

const Profile: React.FC = () => {
  const ProfileDescription = {
    bio: "My name is massimo and this is my first react project",
    name: "Massimo Malone",
  };

  return (
    <div className="profile-page-content">
      <div className="profile-info-group">
        <div className="profile_pic">
          <img src={profileImage} alt="Profile" className="profile-img" />
        </div>
        <div className="page_name">{ProfileDescription.name}'s PAGE</div>
      </div>
      <div className="smack-area-wrapper">
        <CreateSmack />
      </div>
    </div>
  );
};
export default Profile;
