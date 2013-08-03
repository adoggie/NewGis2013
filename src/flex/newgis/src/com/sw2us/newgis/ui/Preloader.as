package com.sw2us.newgis.ui
{
import mx.preloaders.DownloadProgressBar;
import flash.display.Sprite;
import flash.events.ProgressEvent;
import flash.events.Event;
import mx.events.FlexEvent;
import mx.managers.SystemManager;
import mx.managers.BrowserManager;
import flash.utils.Timer;
import flash.events.TimerEvent;

public class Preloader extends DownloadProgressBar
{
public var m_Progress: ProgressBar;
private var m_Timer: Timer;

public function Preloader(): void{
super();
var browser: BrowserManager;
m_Progress = new ProgressBar;
this.addChild(m_Progress);
m_Timer = new Timer(1);
m_Timer.addEventListener(TimerEvent.TIMER, timerEventHandler);
m_Timer.start();
}
override public function set preloader(value:Sprite):void{
value.addEventListener(ProgressEvent.PROGRESS, progressEventHandler);
value.addEventListener(Event.COMPLETE, completeEventHandler);
value.addEventListener(FlexEvent.INIT_PROGRESS, initProgressEventHandler);
value.addEventListener(FlexEvent.INIT_COMPLETE, initCompleteEventHandler);
}
private function progressEventHandler(event: ProgressEvent): void{
var progress: Number = event.bytesLoaded / event.bytesTotal * 100;
if (m_Progress){
m_Progress.progress = progress;
}
}
private function timerEventHandler(event: TimerEvent): void{
this.stage.addChild(this);
var width: Number = this.stage.stageWidth * 40 / 100; // Get 40% for the Stage width
// Set the Position of the Progress bar to the middle of the screen
m_Progress.x = (this.stage.stageWidth - m_Progress.getWidth()) / 2;
m_Progress.y = (this.stage.stageHeight - m_Progress.getHeight()) / 2;
m_Progress.refreshProgressBar();
}
private function completeEventHandler(event: Event): void{
var i: int = 0;
}
private function initProgressEventHandler(event: FlexEvent): void{
var i: int = 0;
}
private function initCompleteEventHandler(event: FlexEvent): void{
m_Progress.ready = true;
m_Timer.stop();
this.dispatchEvent(new Event(Event.COMPLETE));
}
}
} 