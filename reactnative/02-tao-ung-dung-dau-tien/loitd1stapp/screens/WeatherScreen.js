import React from 'react';
import {View, Text, Image, 
    StyleSheet, TextInput, 
    KeyboardAvoidingView,
    ImageBackground
} from 'react-native'

export default class WeatherScreen extends React.Component{
    // define static methods
    static navigationOptions = {
        header: null,
    };
    
    // begin render
    render() {
        return (
            <KeyboardAvoidingView style={mstyles.container} behavior="padding">       
            {/* <View style={mstyles.container}> */}
                <ImageBackground 
                source={require('../assets/images/background.jpg')}
                style={mstyles.imgcontainer}
                imageStyle={mstyles.img}>
                    <View style={mstyles.content}>
                        <Text style={mstyles.heading1}>Hà Nội</Text>
                        <Text style={mstyles.small}>Sunny</Text>
                        <Text style={mstyles.heading1}>23°C</Text>
                        
                        <TextInput placeholder="Tìm kiếm địa danh bất kỳ"
                        placeholderTextColor="white"
                        clearButtonMode="always"
                        style={mstyles.textinp}/>
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
    },
    heading1: {
        fontSize: 44,
        lineHeight: 50,
        color: 'yellow',
        paddingHorizontal: 10,
        paddingVertical: 10,
    },
    small: {
        fontSize: 18,
        lineHeight: 22,
        color: 'yellow',
    },
    textinp: {
        backgroundColor: '#666',
        height: 40,
        width: 300,
        alignSelf: 'center',
        paddingHorizontal: 10,
        marginHorizontal: 20,
        marginTop: 150,
    },
    
});