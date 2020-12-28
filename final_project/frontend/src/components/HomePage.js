import React, {Component} from "react";
import CreateRoom from "./CreateRoom"
import RoomJoinPage from "./RoomJoinPage"
import Room from "./Room"
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom"

export default class HomePage extends Component {
    constructor(props){
        super(props);
    }
    render() {
        return (<Router>

            <Switch>
                <Route exact path='/'>
                    <h1>This is the HomePage</h1>
                </Route>
                <Route path='/join' component={RoomJoinPage} />
                <Route path='/create' component={CreateRoom} />
                <Route path='/room/:roomCode' component={Room} />

            </Switch>

        </Router>);
    }
}