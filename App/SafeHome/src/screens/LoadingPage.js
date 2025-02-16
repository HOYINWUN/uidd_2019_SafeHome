import React, { Component } from 'react';
import { StyleSheet, View, Animated, TouchableOpacity, Image, Easing } from 'react-native';
import { createStackNavigator } from 'react-navigation'
import LoginPage from './Main/LoginPage';
import RegisterPage from './Main/RegisterPage';

class LoadingPage extends Component {
    static navigationOptions = {
        header: null
    };
    constructor(props) {
        super(props);
        this.state = {
            isOverlayVisible: true,
            backgroundColorContainer: "#FFFFFF",
            signedIn: false,
            loginUserType: 2,
            animationComponent: []
        }
        this.springAnimationXY = new Animated.ValueXY({ x: 0, y: 1000 })
    }

    cheakIfLoginBefore = () => {
        if(this.state.signedIn == true) {
            this.login(this.state.loginUserType);
        }
        else {
            this.setState({
                animationComponent: <LoginPage 
                                        login={(loginUserType)=>this.login(loginUserType)}
                                        navigation={() => this.props.navigation.navigate('RegisterPage')}/>});
        }
    }

    /* For slide down the SafeHome icon */
    slideDown = () => {
        this.cheakIfLoginBefore();
        Animated.spring(
            this.springAnimationXY, {
                toValue: { x: 0, y: 0 },
            }
        ).start();
        this.setState({ backgroundColorContainer: "grey" });
        if (this.interval)  // Remove the timer
            clearInterval(this.interval);
    }

    /* If user doesn't click SafeHome icon after 3 seconds, automatically slide down it */
    setTimerlideDown = () => {
        this.interval = setInterval(this.slideDown, 1500);
    }
  
    login(loginUserType) {
        switch (loginUserType) {
            /* For householder */
            case 1:
                alert("Householder page is build in progress");
                break;
            /* For volunteer */
            case 2:
                this.props.navigation.navigate('VolunteerBottomTabNavigation');
                break;
            /* For technician */
            case 3:
                alert("Technician page is build in progress");
                break;
            default:
                alert("Type not found");
        }
    }



    render() {
        return (
            <TouchableOpacity style={[styles.container, { backgroundColor: this.state.backgroundColorContainer }]}
                onPress={this.slideDown}
                onLayout={this.setTimerlideDown}
                activeOpacity={1}>
                <View style={{ position: "absolute" }}>
                    <Image
                        source={require('../../assets/img/plainorange-07.png')}
                        style={{ height: 100, width: 100 }}
                    />
                </View>
                <Animated.View style={[styles.container, this.springAnimationXY.getLayout()]}>
                    { this.state.animationComponent }     
                </Animated.View>
            </TouchableOpacity>
        );
    }
}

const MainRegisterPageStackNavigation = createStackNavigator({
    LoadingPage: {
        screen: LoadingPage,
    },
    RegisterPage: {
        screen: RegisterPage,
    },
},{
    transitionConfig: () => ({
        transitionSpec: {
            duration: 300,
            easing: Easing.out(Easing.poly(4)),
            timing: Animated.timing,
        },
        screenInterpolator: sceneProps => {
            const { layout, position, scene } = sceneProps;
            const { index } = scene;
            const Width = layout.initWidth;
            const translateX = position.interpolate({
                inputRange: [index - 1, index, index + 1],
                outputRange: [Width, 0, -(Width - 10)],
            });
            const opacity = position.interpolate({
                inputRange: [index - 1, index - 0.99, index],
                outputRange: [0, 1, 1],
            });
            return { opacity, transform: [{translateX}] };
        }
    })
});

const styles = StyleSheet.create({
    container: {
        alignItems: 'center',
        justifyContent: 'center',
        width: "100%",
        height: "100%",
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: "grey",
        zIndex: 0,
    },
})

export default MainRegisterPageStackNavigation;