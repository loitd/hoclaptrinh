import React from 'react';
import {StyleSheet, TextInput, View} from 'react-native';

export default class SearchInput extends React.Component{
    // property initializers: Supported by Babel36, property initializers are still in the proposal phase
    // This allows us to declare the member methods as arrow functions
    handleTxtChanged = (newloc) => {
        // This is where we can use a component’s state.
        // We can use the constructor method to to initialize our component-specific data, or state
        this.props.location = newloc;
    }
    render(){
        // Storing local data
        const {placeholder} = this.props;
        const {text} = this.state;
        return(
            <View style={mstyles.container}>
                <TextInput autoCorrect={false}
                placeholder={placeholder}
                placeholderTextColor={this.props.placeholderTextColor}
                clearButtonMode='always'
                value={text}
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