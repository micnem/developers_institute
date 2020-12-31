import React, { Component } from "react";
import { Grid, Button, Typography } from "@material-ui/core";
import CreateRoom from "./CreateRoom"

export default class Room extends Component {
  constructor(props) {
    super(props);
    this.state = {
      votesToSkip: 2,
      guestCanPause: false,
      isHost: false,
      showSettings: false,
      spotifyAuthenticated: false,
    };
    this.roomCode = this.props.match.params.roomCode;
    this.leaveButtonPressed = this.leaveButtonPressed.bind(this);
    this.showSettings = this.showSettings.bind(this);
    this.renderSettings = this.renderSettings.bind(this);
    this.renderSettingsButton = this.renderSettingsButton.bind(this);
    this.getRoomDetails= this.getRoomDetails.bind(this);
    this.authenticateSpotify = this.authenticateSpotify.bind(this);
    this.getRoomDetails();
  }

  authenticateSpotify(){
    fetch('/splat/is-authenticated')
    .then((response) => response.json())
    .then((data)=>{
      this.setState({spotifyAuthenticated: data.status});
      if (!data.status) {
        fetch("/splat/get-auth-url")
        .then((response) => response.json())
        .then((data) => {
          window.location.replace(data.url);
        })
      }
    })
  }
  getRoomDetails() {
    return fetch("/api/get-room" + "?code=" + this.roomCode)
      .then((response) => {
        if (!response.ok) {
          this.props.leaveRoomCallback();
          this.props.history.push("/");
        }
        return response.json();
      })
      .then((data) => {
        this.setState({
          votesToSkip: data.votes_to_skip,
          guestCanPause: data.guest_can_pause,
          isHost: data.is_host,
        });
        this.authenticateSpotify();
      });
  }

  leaveButtonPressed() {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
    };
    fetch("/api/leave-room", requestOptions).then((_response) => {
      this.props.leaveRoomCallback();
      this.props.history.push("/");
    });
  }
  showSettings(value) {
    this.setState({
      showSettings: value,
    });
  }

  renderSettings(){
    return(
      <Grid container spacing={1}>
          <Grid item xs={12} align="center">
            <CreateRoom update={true} votesToSkip={this.state.votesToSkip} guestCanPause={this.state.guestCanPause} roomCode ={this.roomCode} updateCallback={this.getRoomDetails}></CreateRoom>
          </Grid>
          <Grid item xs={12} align="center"> </Grid>
          <Grid item xs={12} align="center">
          <Button variant="contained" color="secondary" onClick={()=> this.showSettings(false)}>Close</Button>
        </Grid>
      </Grid>
    );
  }

  renderSettingsButton() {
    return (
      <Grid item xs={12} align="center">
        <Button variant="contained" color="primary" onClick={()=> this.showSettings(true)}>Settings</Button>
      </Grid>
    )
  }

  render() {
    if (this.state.showSettings) {
      return this.renderSettings();
    }
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography variant="h4" component="h4">
            Code: {this.roomCode}
          </Typography>
        </Grid>     
        <Grid item xs={12} align="center">
          <Typography variant="h6" component="h6">
            Votes: {this.state.votesToSkip}
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <Typography variant="h6" component="h6">
            Guest Can Pause: {this.state.guestCanPause.toString()}
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <Typography variant="h6" component="h6">
            Host: {this.state.isHost.toString()}
          </Typography>
        </Grid>
        {this.state.isHost ? this.renderSettingsButton() : null}
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="secondary"
            onClick={this.leaveButtonPressed}
          >
            Leave Room
          </Button>
        </Grid>
      </Grid>
    );
  }
}