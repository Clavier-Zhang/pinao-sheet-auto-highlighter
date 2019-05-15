import React from "react";
import ReactDOM from "react-dom";
import { HashRouter as Router, Route, Switch } from "react-router-dom";
import Dashboard from "./Dashboard.jsx";

ReactDOM.render(
    <Router>
        <Switch>
            <Route path={'/'} component={Dashboard}/>;
        </Switch>
    </Router>,
    document.getElementById("root")
);
