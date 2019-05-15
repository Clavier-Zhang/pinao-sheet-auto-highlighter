import React, {Component} from "react";

import Grid from "@material-ui/core/Grid";
import sample from './output.pdf'

import { Document, Page } from 'react-pdf';


class App extends Component {

    state = {
        file: false
    }

    render() {
        return (
            <Grid container>

                <input type='file' accept='*' onChange={(file) => {
                    console.log(file.target.files[0])
                    this.setState({file: file.target.files[0]})
                }}/>>

                <div>
                    <Document
                    file={this.state.file ? this.state.file : sample}
                    // onLoadSuccess={this.onDocumentLoadSuccess}
                    >
                    <Page pageNumber={1} />
                    </Document>
                    <p>Page {1} of {3}</p>
                </div>

            </Grid>
        );
    }
}

export default App;
