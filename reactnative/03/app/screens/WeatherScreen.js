// --------------------------------------
// React Native Lesson 04
// youtube.com/tranducloi
// --------------------------------------
import React from 'react';
import {View, Text, Image, 
    StyleSheet, TextInput, 
    KeyboardAvoidingView,
    ImageBackground, Platform
} from 'react-native';
import SearchInput from '../components/SearchInput'

export default class WeatherScreen extends React.Component{
    // define static methods
    static navigationOptions = {
        header: null,
    };
    
    // begin render
    render() {
        // default location
        const location = 'Hà Nội';

        return (
            <KeyboardAvoidingView style={mstyles.container} behavior="padding">       
            {/* <View style={mstyles.container}> */}
                <ImageBackground 
                source={require('../assets/images/background.jpg')}
                style={mstyles.imgcontainer}
                imageStyle={mstyles.img}>
                    <View style={mstyles.content}>
                        <Text style={[mstyles.h1, mstyles.txt]}>{location}</Text>
                        <Text style={[mstyles.small, mstyles.txt]}>Sunny</Text>
                        <Text style={[mstyles.h2, mstyles.txt]}>23°C</Text>
                        
                        <SearchInput placeholder="Tìm kiếm địa danh"
                        placeholderTextColor="black"/>
                        {/* The way we call image in React Native */}
                        {/* <Image source={require('../assets/images/background.jpg')} style={mstyles.backgroundimg} /> */}

                    </View>
                </ImageBackground>
            {/* </View> */}
            </KeyboardAvoidingView>
        );
    }

}

// begin defining styles
const mstyles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#34495E',
        // alignItems: 'center',
        // justifyContent: 'center',
    },
    imgcontainer:{
        flex: 1,
    },
    img:{
        flex: 1,
        width: null,
        height: null,
        resizeMode: 'cover',
    },
    content: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'rgba(0,0,0,0.275)', //for overlay
    },
    txt: {
        fontFamily: Platform.OS === 'ios' ? 'AvenirNext-Regular' : 'Roboto',
        paddingHorizontal: 10,
        paddingVertical: 10,
    },
    h1: {
        fontSize: 44,
        lineHeight: 50,
        color: 'yellow',
        fontWeight: 'bold',
    },
    h2: {
        fontSize: 38,
        lineHeight: 44,
        color: 'yellow',
    },
    small: {
        fontSize: 18,
        lineHeight: 22,
        color: 'yellow',
    },
});