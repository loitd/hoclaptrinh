import React from 'react';
import {StyleSheet, TextInput, View} from 'react-native';

// props are immutable and are always“owned” by a component’s parent while state can be mutated and is “owned” by the component itself. 
// This is an extremely important pattern to remember while building components with React Native.
// 
export default class SearchInput extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            location: '',
        };
    }
    // This allows us to declare the member methods as arrow functions
    handleTxtChanged = (txt) => {
        // React provides components with the method setState() to do this. In addition to mutating the
        // component’s state object, this method triggers the React component to re-render, which is essential
        // after the state changes
        this.setState({ location: txt, })
    }

    handleTxtSubmitted = (txt) => {
        // onSubmit is a function of component props
        const {onSubmit} = this.props;
        const {location} = this.state;

        if (!location) return;

        onSubmit(location);
        //reset location
        this.setState({location: ''});
        //
    }
    render(){
        // Storing local data
        const {placeholder} = this.props;
        const {location} = this.state;
        return(
            <View style={mstyles.container}>
                <TextInput autoCorrect={false}
                placeholder={placeholder}
                placeholderTextColor={this.props.placeholderTextColor}
                clearButtonMode='always'
                value={location}
                onChangeText={this.handleTxtChanged}
                onSubmitEditing={this.handleTxtSubmitted}></TextInput>
            </View>
        );
    }
}

const mstyles = StyleSheet.create({
    container: {
        backgroundColor: '#FBBC04',
        height: 40,
        borderRadius: 9,
        paddingHorizontal: 10,
        marginHorizontal: 20,
        marginTop: 200,
        alignItems: 'center',
        justifyContent: 'center',
        width: 300,
    },
    txtInput: {
        flex: 1,
        color: 'black',
    }
});